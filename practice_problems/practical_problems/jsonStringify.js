/*

❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object and return the JSON representation of the object as a string. This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
{x: 5, y: "Oliver"}
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
- iterate over javascript object
- convert everything into a string essentially
- how do we check for nested objects?

Time: O(n)
Space: O(1) if there's no need to preserve the original object
 

📆 PLAN
Outline of algorithm #: 

- iterate over object
- for both keys and values
    - check if it's a string
    - if it's not convert it to one
 

🛠️ IMPLEMENT
function stringify(obj) {
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

*/

function stringify(obj) {
    for (let key in obj) {
        let value = obj[key]
        if (typeof key !== "string") {
            let newKey = key.toString()
            obj[newKey] = value
            delete obj[key]
            key = newKey
        }
        if (typeof value !== "string") {
            value = value.toString()
            obj[key]
        }
    }

    return obj
}

obj = {
    name: "John",
    age: 25
}

console.log(stringify(obj))