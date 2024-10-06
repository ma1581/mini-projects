package com.example.PollingApp;


public class Result {

    private String option;
    private long voteCount;

    // Constructors, getters, setters, etc.

    public Result(String option, long voteCount) {
        this.option = option;
        this.voteCount = voteCount;
    }

    public String getOption() {
        return option;
    }

    public void setOption(String option) {
        this.option = option;
    }

    public long getVoteCount() {
        return voteCount;
    }

    public void setVoteCount(long voteCount) {
        this.voteCount = voteCount;
    }
}
