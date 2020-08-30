/*
    This is a basic JavaScript file with which to test the application with
*/

class Hospital {
    constructor() {
        this.doctor = new Doctor("John");
        this.nurse = new Nurse("Jane");
        this.allMyPatients = [];
    }

    admitAPatient() {
        this.allMyPatients.push(new Patient());
    }

    treatPatient() {
        for (aPatient in this.allMyPatients) {
            this.doctor.check(aPatient);
            this.nurse.cure(aPatient);
        }
    }

    dischargeAPatient() {
        this.allMyPatients.shift();
    }
}

class Doctor {
    constructor(name) {
        this.name = name;
    }

    check(patient) {
        patient.tellSymptons();
    }
}

class Nurse {
    constructor(name) {
        this.name = name;
    }

    cure(patient) {
        patient.feelBetter();
    }
}

class Patient {
    constructor(issue) {
        this.issue = issue;
    }

    tellSymptons() {
        return this.issue;
    }

    feelBetter() {
        this.issue = null;
    }
}