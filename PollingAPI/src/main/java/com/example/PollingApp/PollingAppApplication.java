package com.example.PollingApp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.reactive.function.client.WebClient;
import java.util.Scanner;

@SpringBootApplication
public class PollingAppApplication {


 private static final String BASE_URL = "http://localhost:8080/api"; // Replace with your API base URL

    public static void main(String[] args) {
        SpringApplication.run(PollingAppApplication.class, args); 
    }
}
