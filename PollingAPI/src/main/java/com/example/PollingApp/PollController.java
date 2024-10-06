package com.example.PollingApp;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

//@RestController
//@RequestMapping("/api/polls")
//public class PollController {
//
//    @Autowired
//    private PollService pollService;
//
//    @PostMapping
//    public Poll createPoll(@RequestBody Poll poll) {
//    	System.out.println("Coming here");
//        return pollService.createPoll(poll);
//    }
//
//    @PostMapping("/{pollId}/vote")
//    public void vote(@PathVariable Long pollId, @RequestParam String selectedOption) {
//        pollService.vote(pollId, selectedOption);
//    }
//
//    @GetMapping("/{pollId}/results")
//    public List<Result> getResults(@PathVariable Long pollId) {
//        return pollService.getResults(pollId);
//    }
//}



@RestController
@RequestMapping("/api/polls")
public class PollController {

    @Autowired
    private PollService pollService;

    @PostMapping
    public Poll createPoll(@RequestBody Poll poll) {
        return pollService.createPoll(poll);
    }

    @PostMapping("/{pollId}/vote")
    public void vote(@PathVariable Long pollId, @RequestParam String selectedOption) {
        pollService.vote(pollId, selectedOption);
    }

    @GetMapping("/{pollId}/results")
    public List<Result> getResults(@PathVariable Long pollId) {
    	System.out.println("Getting results");
        return pollService.getResults(pollId);
    }
    
    @GetMapping
    public List<Poll> getAllPolls() {
        return pollService.getAllPolls();
    }
}

