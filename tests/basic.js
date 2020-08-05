class Patient {
    constructor(issue) {
        this.issue = new Object();
    }

    tellSymptons() {
        return this.issue;
    }

    feelBetter() {
        this.issue = new Object();
    }
}