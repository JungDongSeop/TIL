리액트 라우터 사용



```react
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);

reportWebVitals();

```

App.js

```react
import { Route, Routes } from "react-router-dom";
import Main from "./components/main/Main";
import Login from "./components/auth/login/Login";
import Signup from "./components/auth/signup/Signup";
import "./App.css";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
    </Routes>
  );
}

export default App;
```

Main.js

```react
import classes from "./Main.module.css";
import { Link } from "react-router-dom";

const Main = () => {
  return (
    <div className={classes.main}>
      <h1>메인 페이지. 제일 처음 보이는 화면입니다.</h1>
      <p><Link to="/login">로그인 이동</Link></p>
      <p><Link to="/signup">회원가입 이동</Link></p>
    </div>
  );
};

export default Main;
```

Login.js

```react
const Login = () => {
  return (
    <div>
      <h2>
        로그인 기능 구현합시다.
      </h2>
    </div>
  );
};

export default Login;
```





## URL 쿼리스트링 사용

- URL 파라미터에서 `/profiles/:username` 같이 경로 작성



App.js

```react
import { Route, Routes } from "react-router-dom";
import Main from "./components/main/Main";
import MyPage from "./components/mypage/MyPage";
import "./App.css";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Main />} />
      <Route path="/mypage/:username" element={<MyPage />} />
    </Routes>
  );
}

export default App;
```

MyPage.js

```react
import { useParams } from "react-router-dom";

const data = {
  dongsum: {
    name: "Dongsum",
    description: '동섬이 설명',
  },
  sumin: {
    name: "Sumin",
    description: '수민이 설명',
  },
};

const MyPage = () => {
  const params = useParams();
  const profile = data[params.username];

  return (
    <div>
      <h1>마이페이지 입니다.</h1>
      {profile ? (
        <div>
          <h2>{profile.name}</h2>
          <p>{profile.description}</p>
        </div>
      ) : (
        <p>존재하지 않는 프로필입니다</p>
      )}
    </div>
  );
};

export default MyPage;
```



쿼리스트링을 브라우저 화면에 띄우는 법 : `location.search`

- `pathname` : 현재 주소 경로 (쿼리스트링 제외)
- `search` : `?`를 포함한 쿼리스트링 값
- `hash` : 주소의 `#` 문자열 뒤
- `state` : 페이지로 이동할 때 임의로 넣을 수 있는 상태 값
- `key` : location 객체의 고유값

```react
return (
	<div>
    	<p>쿼리스트링 : {location.search} </p>
    </div>
)
```



이후 `onSearchParams`를 써서 쉽게 파싱 가능 (p336 참조)



### 중첩된 라우트

?? 책 340 보기



## 리액트 라우터 부가 기능



`useNavigate`

- Link 컴포넌트 쓰지 않고 다른 페이지로 이동할 때 사용 (버튼 등)
- 함수 등에서 사용



`NavLink`

- 링크에서 사용하는 경로가 현재 라우트의 경로와 일치하는 경우 특정 스타일 또는 CSS 클래스를 적용하는 컴포넌트
- 게시글 목록에서 현재 게시글 페이지에 들어와있는 경우, 강조 기능에 사용 가능



### 404 페이지 만들기
