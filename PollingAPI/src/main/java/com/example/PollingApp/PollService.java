package com.example.PollingApp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.data.domain.Sort;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PollService {

    @Autowired
    private PollRepository pollRepository;

    @Autowired
    private VoteRepository voteRepository;

    public Poll createPoll(Poll poll) {
        return pollRepository.save(poll);
    }

    public void vote(Long pollId, String selectedOption) {
        Poll poll = pollRepository.findById(pollId).orElseThrow(() -> new RuntimeException("Poll not found"));
        Vote vote = new Vote();
        vote.setPoll(poll);
        vote.setSelectedOption(selectedOption);
        voteRepository.save(vote);
    }

    public List<Result> getResults(Long pollId) {
        Poll poll = pollRepository.findById(pollId).orElseThrow(() -> new RuntimeException("Poll not found"));

        List<Result> results = new ArrayList<>();

        for (String option : poll.getOptions()) {
            long voteCount = voteRepository.countByPollIdAndSelectedOption(pollId, option);
            results.add(new Result(option, voteCount));
        }

        return results;
    }
    public List<Poll> getAllPolls() {
        return pollRepository.findAll();
    }
    
    

}
