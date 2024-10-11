// In JavaScript, objects are typically used in place of dictionaries, similar to how Python uses dictionaries. JavaScript objects store key-value pairs, and the syntax you've used is mostly correct, except for a few adjustments.

// Here’s what you need to know:

// ### Objects as Dictionaries in JavaScript
// - **JavaScript objects** act like dictionaries in Python, where you can use keys (in this case, words) to store and retrieve values (like word counts).
// - JavaScript does not have a `.dictionary()` method. Instead, you directly access or create key-value pairs using square brackets (`[]`) or dot notation (`.`).

// So, the corrected version of your `add` function is:

// ```javascript
// add(word = "") {
//   word = word.toLowerCase();
// Use 'word' as the key and increment its value in word_counts
//   this.word_counts[word] = (this.word_counts[word] || 0) + 1;
// }
// ```

// ### Explanation:
// - `this.word_counts[word]`: This syntax is used to access or set a key in the `word_counts` object. If the `word` exists as a key, its value is retrieved. If it doesn’t exist, JavaScript returns `undefined`.
// - `(this.word_counts[word] || 0)`: If `word` exists, its value is used. If `word` doesn’t exist, `0` is returned by default, which is then incremented by `1`.

// ### Using Object Properties After `.`
// When you type `this.word_counts.` in JavaScript, you’ll see all the default methods and properties available for objects, like `.hasOwnProperty()`, `.keys()`, etc. JavaScript doesn’t have built-in methods like Python’s `get()` for objects, but you can still achieve similar functionality using JavaScript's available methods.

// #### Object Methods You Can Use:
// 1. **`Object.keys()`**: Get an array of the object's keys.
//    ```javascript
//    Object.keys(this.word_counts);
//    ```
// 2. **`Object.values()`**: Get an array of the object's values.
//    ```javascript
//    Object.values(this.word_counts);
//    ```
// 3. **`Object.entries()`**: Get an array of key-value pairs.
//    ```javascript
//    Object.entries(this.word_counts);
//    ```

// ### Sorting Objects
// If you want to **sort** the `word_counts` object by its keys or values, JavaScript doesn’t have a direct method to sort objects. However, you can convert the object into an array of key-value pairs using `Object.entries()`, sort the array, and then convert it back to an object.

// Here’s how to sort the word counts by their values:

// ```javascript
// const sortedCounts = Object.entries(this.word_counts)
//   .sort(([, a], [, b]) => b - a); // Sort by value in descending order

// console.log(sortedCounts);
// ```

// ### Example of Sorting:

// ```javascript
// const counter = new WordCounter();
// counter.add("Hello");
// counter.add("World");
// counter.add("hello");
// counter.add("WORLD");
// counter.add("JavaScript");

// // Sorting the word counts by their count values in descending order
// const sortedCounts = Object.entries(counter.word_counts)
//   .sort(([, a], [, b]) => b - a);

// console.log(sortedCounts);
// ```

// ### Output:
// ```javascript
// [
//   ['hello', 2],
//   ['world', 2],
//   ['javascript', 1]
// ]
// ```

// This way, you can sort the word counts and manipulate the object further. Let me know if you need more clarity or functionality!

// Exercise 1

// class WordCounter {
//   constructor() {
//     // this?.tags = tags;
//     this.word_counts = {};
//   }
//   add(word = "") {
//     word = word.toLowerCase();
//     this.word_counts[word] = (this.word_counts[word] || 0) + 1;
//   }
// }
// const counter = new WordCounter();
// counter.add("Hello");
// counter.add("World");
// counter.add("hello");
// counter.add("WORLD");
// counter.add("JavaScript");

// console.log(counter);

class WordCounter {
  constructor() {
    this.wordCounts = {};
  }

  add(word = "") {
    word = word.toLowerCase();
    this.wordCounts[word] = (this.wordCounts[word] || 0) + 1;
  }
  count(word = "") {
    return this.wordCounts[word.toLowerCase()] || 0;
  }
}
const counter = new WordCounter();
const sentence = "Python is great and Python is fun";
for (let word of sentence.split(" ")) {
  counter.add(word);
}
console.log(counter.wordCounts);
console.log(counter.count("python"));
