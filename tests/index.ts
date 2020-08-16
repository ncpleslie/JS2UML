class TestClass {
    private aValue: Object;
    private testValue: number;
    constructor() {
        this.aValue = new Object();
        this.testValue = 1;
    }

    aFunction(someValue: string): void {
        console.log(this.aValue);
    }
}