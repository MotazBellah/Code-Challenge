// The goal of this exercise is to convert a string to a new string where
// each character in the new string is
// "(" if that character appears only once in the original string,
// or ")" if that character appears more than once in the original string.
// Ignore capitalization when determining if a character is a duplicate.

function duplicateEncode(word){
    var newArra = [];
            var wordArr = word.toLowerCase().split("");
            var x;
            for (var i = 0; i < wordArr.length; i++) {
                x = searchElement(wordArr, wordArr[i])
                if(x.length > 1){
                    newArra.push(')');
                }
                else {
                    newArra.push('(');
                }
            }
            return newArra.join("");
}
function searchElement(arr, str) {
    var elementPosition = [], startsearchAt = 0;
    var foundAt;
    do {

      foundAt = arr.indexOf(str, startsearchAt);
      if (foundAt != -1) {
        elementPosition.push(foundAt);
        startsearchAt = foundAt + 1;
         }

     } while (foundAt != -1);

       return elementPosition;
 }
