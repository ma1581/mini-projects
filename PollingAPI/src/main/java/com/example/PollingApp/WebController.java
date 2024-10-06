package com.example.PollingApp;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.reactive.function.client.WebClient;

import java.util.List;

@Controller
public class WebController {

    private final String POLL_API_URL = "http://localhost:8080/api/polls";

    @Autowired
    private WebClient.Builder webClientBuilder;

    @GetMapping("/")
    public String home(Model model) {
        // Fetch polls from the API using WebClient
        List<Poll> polls = webClientBuilder.build()
                .get()
                .uri(POLL_API_URL)
                .retrieve()
                .bodyToFlux(Poll.class)
                .collectList()
                .block();

        model.addAttribute("polls", polls);
        System.out.println("Loading html");
        return "index";
    }
}

