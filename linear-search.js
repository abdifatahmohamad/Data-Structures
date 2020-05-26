/* Linear Search takes two arguments. First the item you looking for
(doesn't necessarily have to be sorted), second the item that you're looking for*/

/* TASK: Implement Linear Search: Create a function that looks through 
the array to find the value 90 and it returns array */

function linearSearch(list, item) {
	// -1 means it wasn't found
	let index = -1;
	list.forEach((listItem, i) => {
		if (listItem === item) {
			//This will always return the last index if there's a duplicate
			index = i;
		}
	});
	//if it doesn't find anything, it will return -1
	return index;
}

console.log(linearSearch([2, 6, 7, 90, 103], 90));
//Output 3
//The time complexity: Linear: O(n)


