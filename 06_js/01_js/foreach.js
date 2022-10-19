// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
    console.log(color)
}

colors.forEach(printClr)

// 2.   python 의 map 함수와 비슷
colors.forEach(function (color) {
    console.log(color)
})

// 3.
colors.forEach((color) => {
    console.log(color)
})












