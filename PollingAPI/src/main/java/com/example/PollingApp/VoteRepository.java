package com.example.PollingApp;

import org.springframework.data.jpa.repository.JpaRepository;

public interface VoteRepository extends JpaRepository<Vote, Long> {
    long countByPollIdAndSelectedOption(Long pollId, String selectedOption);

}
