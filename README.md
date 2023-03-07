# thywordle-solution-generator

A Python script and web scraper to generate [ThyWordle](https://github.com/FHU/thywordle) solution objects

## How to Run

- Download or clone the repo and cd into `thywordle-solution-generator`
- In a terminal, run `python solution-generator.py`

### Responding to the Prompts

#### Generating a Single Solution

- Run the script
- When the prompt asks if you only want to generate a single solution for one verse, respond with `Y`
- Then enter the reference of the Bible verse (i.e., `Matthew 1:1`, `Acts 2:38`, `Philemon 4`)
- Copy the response outputted by the script to use elsewhere

#### Generating an Array of Solution Objects

- Open the repo and open the file: `reference_lists/newSolutionsList.py`
- Add as many Bible references as you would like to the `newSolutionsList` array (ensure that each reference is a valid Bible verse)
- Run the script
- When the prompt asks if you only want to generate a single solution for one verse, respond with `N`
- The program will then direct you to open a `json` file beginning with `newReferenceList` in the home directory
- Copy the array of Solution Objects to use elsewhere
