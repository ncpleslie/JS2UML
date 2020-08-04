class Patient {
    constructor(issue) {
        this.issue = issue;
    }

    tellSymptons() {
        return this.issue;
    }

    feelBetter() {
        this.issue = new Object();
    }
}