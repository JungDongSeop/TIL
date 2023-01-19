- useState : 함수 컴포넌트에서도 가변적인 상태 관리
- useEffect : 렌더링 직후 작업을 설정



예시

```js
import { useState } from "react";

const Counter = () => {
  const [plusValue, setPlusValue] = useState(0);
  const [minusValue, setMinusValue] = useState(0);

  return (
    <div>
      <p>
        현재 카운터 값은 {plusValue}, {minusValue}입니다.
      </p>
      <button onClick={() => setPlusValue(plusValue + 1)}>+1</button>
      <button onClick={() => setMinusValue(minusValue - 1)}>-1</button>
    </div>
  )
}

export default Counter
```



- 설명
  - `const [value, setValue] = useState(0);` 형태로 사용
  - `useState` 함수의 파라미터에는 기본값 `0` 입력
  - `useState` 함수가 호출되면, 배열을 반환
  - `value` : 상태값, `setValue` : 상태를 설정하는 함수. 이 함수의 인자로 상태값이 변경됨



useEffect 사용하기

- 설명

  - `useEffect` : 컴포넌트가 렌더링될 때마다 특정 작업을 수행하도록 설정 가능한 Hook

- 예시

  - 함수 안에 아래와 같이 작성

  - ```js
      useEffect(() => {
        console.log('렌더링 완료')
        console.log(plusValue, minusValue)    
      })
    ```

- 특정 값이 업데이트될 때만 실행하고 싶으면, `useEffect` 두번째 인자에 검사할 특정 값 입력

  - ```js
    useEffect(() => {
        console.log(name)
    }, [name])
    ```



그 외

- useReducer, useMemo, useCallback, useRef

