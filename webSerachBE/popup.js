document.addEventListener("DOMContentLoaded", function () {
  const text = document.querySelector(".text");
  const searchInput = document.querySelector(".searchTerm");

  const highlightButton = document.createElement("button");
  highlightButton.textContent = "Highlight";
  highlightButton.id = "highlightButton";

  document.body.appendChild(highlightButton);

  highlightButton.addEventListener("click", function () {
    // Get the search text from the input field
    const searchText = searchInput.value;

    // Create a KMP object
    const kmp = new KMP(searchText);

    // Get the indexes of all the occurrences of the search text
    const occurrences = kmp.search(text.textContent);

    // Check if there are any occurrences
    if (occurrences.length === 0) {
      // Show an alert message
      alert("No match found");
    } else {
      // Loop through the occurrences and highlight them
      for (const occurrence of occurrences) {
        const start = occurrence[0];
        const end = occurrence[1];

        text.slice(start, end).style.backgroundColor = "yellow";
      }
    }
  });
});

class KMP {
  constructor(searchText) {
    this.searchText = searchText;
    this.lps = this.computeLPSArray();
  }

  search(text) {
    const n = text.length;
    const m = this.searchText.length;

    const occurrences = [];
    var i = 0;
    var j = 0;

    while (i < n) {
      if (text[i] === this.searchText[j]) {
        i++;
        j++;

        if (j === m) {
          occurrences.push([i - j, i]);
          j = this.lps[j - 1];
        }
      } else if (j > 0) {
        j = this.lps[j - 1];
      } else {
        i++;
      }
    }

    return occurrences;
  }

  computeLPSArray() {
    const lps = [];
    const m = this.searchText.length;

    lps[0] = 0;

    for (var i = 1; i < m; i++) {
      var j = lps[i - 1];

      while (j > 0 && this.searchText[i] !== this.searchText[j]) {
        j = lps[j - 1];
      }

      if (this.searchText[i] === this.searchText[j]) {
        j++;
      }

      lps[i] = j;
    }

    return lps;
  }
}
