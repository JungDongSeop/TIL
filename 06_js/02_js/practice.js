// const inputs = [
//   [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
//   [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
//   [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
// ]

// // solution 함수 완성
// function solution(K, N, M, chargers) {
//   let cnt = 0
//   let i = N-K
//   let flag = 0
//   while (i > 0) {
//     flag = 0
//     // console.log(i)
//     for (let idx = i; idx < i+K; idx++) {
//       if (chargers.find(element => element === idx)) {
//         // console.log('wow')
//         i = idx
//         i -= K
//         cnt += 1
//         flag = 1
//         break
//       }
//       // console.log('no', idx)
      
//     } 
//     if (flag === 1) {
//       continue
//     }
    
//     console.log(0)
//     return
//     // console.log('here')

//   }

//   console.log(cnt)
//   return

// }

// for (const input of inputs) {
//   solution(...input)
// }

let N = 5
for (let i=0; i < N; i++) {
    let arr = ''
    for(let j = 0; j < 2*N; j++) {
        if (j < N-i) {
            arr += ' '
        }
        else if (j > N+i) {
            arr += ' '
        }
        else {
            arr += '*'
        }
           
    }
    console.log(arr)
}