// Returns a hash code (number) for the given string
function stringToNumber(s) {
    let hash = 0;
    for (let i = 0; i < s.length; i++) {
        hash = 31 * hash + s.charCodeAt(i);
    }
    return hash;
}

const items = [
    ["apple", "1.69"],
    ["banana", "0.59"],
    ["orange", "1.99"]
];

const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter name: ", function(inputName) {
    inputName = inputName.trim();
    let found = false;
    for (const item of items) {
        if (item[0].toLowerCase() === inputName.toLowerCase()) {
            console.log("Price:", item[1]);
            found = true;
            break;
        }
    }
    if (!found) {
        console.log("Name not found.");
    }
    readline.close();
});
