let nums = [1, 2, 3, 4, 5];

const reverse = (arr) => {
	for (i = 1; i < arr.length / 2; i++) {
		let intA = arr[i - 1];
		arr[i - 1] = arr[arr.length - i];
		arr[arr.length - i] = intA;
	}
};
console.log(nums);
reverse(nums);
console.log(nums);
