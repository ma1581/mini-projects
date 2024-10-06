package com.example.PollingApp;

import org.springframework.data.jpa.repository.JpaRepository;

public interface PollRepository extends JpaRepository<Poll, Long> {
 // Additional methods if needed
}
