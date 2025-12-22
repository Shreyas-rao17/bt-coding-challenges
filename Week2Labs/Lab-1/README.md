### My findings
- The program demonstrates the concept of encapsulation in object-oriented programming.

- It shows the difference between directly accessing class variables and using properties (getters and setters).

- AccountManager1 accesses the account variables directly, which bypasses the internal logic of the Account class.

- Because of direct access, important rules such as adding the bank code and calculating interest are skipped.

- AccountManager2 uses the property methods of the Account class, so all business rules are applied automatically.

- This is why the account number and balance differ when using the two account managers.

- The example clearly shows why object-oriented programming is better than procedural programming in such scenarios.

- Encapsulation helps protect data, enforce rules, and maintain consistent behavior across the program.