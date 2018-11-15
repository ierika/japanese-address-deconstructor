# Japanese Address Deconstructor API

Splits Japanese addresses into several components such as follows:

- Country
- Postal code
- Prefecture
- City/Ward
- District
- House number
- Floor number
- Building name
- Unit number/name


## Challenges

House number, floor number, and building name will be challenging as people have
their own preference on how to write these information.

By scanning several hundreds or thousands of these addresses, we'll hopefully
be able to make out the pattern. Might have to try Machine Learning techniques
this time...or not.
