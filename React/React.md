https://github.com/facebook/create-react-app 에서 react 설치



index.html

- 브라우저 화면이 표현되는 곳
- `<div id="root"> </div>` 안에 들어가는 코드가 브라우저 화면에 표시
- root 안의 파일들은 src(source) 파일 안에서 참고



### js 코딩

src

- index.js

  - 진입 파일.
  - 이 안을 보면 root div 태그 안을 본다고 명시되어 있음
  - App.js 파일과 연결됨

- App.js

  - 이곳에서 원하는 코드 작성..?

  - 가장 바깥의 div 태그는 반드시 존재해야 함. 그 안에 코드 작성

  - 이번 수업에선 클래스 형태로 작성

  - ```js
    class App extends Component {
      render() {
        return (
          <div className="App">
    		HTML 태그 작성
          </div>
        )
      }
    }
    ```



### CSS 코딩

index.js 파일 안의 `import './index.css';` 부분을 보면, index.css 파일 참조

index.css

- 여기서 css 파일 수정



# 실전

## 컴포넌트

### 컴포넌트 작성

App.js 안에 원하는 이름의 class 작성

이후 아래의 App 클래스에 해당 컴포넌트 추가

```js
class Subject extends Component {
  render() {
    return (
      <header>
        <h1>WEB</h1>
        world wide web
      </header>
    )
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject></Subject>
      </div>
    )
  }
}
```

### Props

```js
class Subject extends Component {
  render() {
    return (
      <header>
        <h1>{this.props.title}</h1>		//여기
        {this.props.sub}
      </header>
    )
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject title="WEB" sub="world wide web!"></Subject>	// 여기
        <TOC></TOC>
        <Content></Content>
      </div>
    )
  }
}
```

### 컴포넌트 파일로 분류하기

컴포넌트가 너무 많아지면, App.js 안에 전부 적기가 힘들다 => 파일로 분류





## STATE

Component 내부에서 사용하는 정보. props와는 철저히 분리됨

props : read-only (하위에서 props 받은 것들 수정 불가능)

state : 수정 가능 (this.setState)

### 사용

`render()` 이전에 `constructor` 작성 시, 컴포넌트 구성할 때 먼저 실행됨



```js
class App extends Component {
  constructor(props) {					// 선언
    super(props)
    this.state = {
      subject:{title:"WEB", sub:"world wide web"}
    }
  }

  render() {
    return (
      <div className="App">
        <Subject 
          title={this.state.subject.title} 		// 사용
          sub={this.state.subject.sub}
        >
        </Subject>
        <TOC></TOC>
        <Content title="HTML" sub="article"></Content>
      </div>
    )
  }
}
```

### key

/Components/TOC.js

```js
import React, { Component } from 'react';

class TOC extends Component{
  render() {							//여기부터
    var lists =  [];
    var data = this.props.data;
    var i = 0;
    while(i < data.length) {
      lists.push(<li key={data[i].id}><a href={"/content/"+data[i].id}>{data[i].title}</a></li>)
      i = i + 1;						//여기까지
    
    }
    return (
      <nav>
        <ul>
          {lists}						//여기 수정
        </ul>
      </nav>  
    )
  }
}

export default TOC;
```

App.js

```js
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {										// 여기서 선언
      subject:{title:"WEB", sub:"world wide web"},
      contents:[
        {id:1, title:'HTML', desc:'HTML is for information'},
        {id:2, title:'CSS', desc:'CSS is for design'},
        {id:3, title:'JS', desc:'JS is for interactive'},
      ]
    }
  }

  render() {
    return (
      <div className="App">
        <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub}
        >
        </Subject>
        <TOC data={this.state.contents}></TOC>			// 여기서 props
        <Content title="HTML" sub="article"></Content>
      </div>
    )
  }
}
```





## 이벤트

브라우저의 역동성을 더함. 동적으로 작동



### 사용

컴포넌트 안의 `render() {여기에 작성}`

 App.js

```js
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      mode:'welcome',
      subject:{title:"WEB", sub:"world wide web"},
      welcome:{title:'Welcome', desc:'Heelo, React!'},
      contents:[
        {id:1, title:'HTML', desc:'HTML is for information'},
        {id:2, title:'CSS', desc:'CSS is for design'},
        {id:3, title:'JS', desc:'JS is for interactive'},
      ]
    }
  }

  render() {
    console.log('App render')
    var _title, _desc = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if(this.state.mode === 'read') {
      _title = this.state.contents[0].title;
      _desc = this.state.contents[0].desc;
      
    }
    return (
      <div className="App">
        <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub}
        >
        </Subject>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} sub={_desc}></Content>
      </div>
    )
  }
}
```



WEB 클릭하면 경고창 띄우기

```js
        <header>
          <h1><a href="/" onClick={function(e){
            console.log(e);	
            e.preventDefault();						// 새로고침 방지
            alert('hi');
          }}>{this.state.subject.title}</a></h1>
          {this.state.subject.sub}
        </header>
```



클릭하면 state 변수 바꾸기

```js
        <header>
          <h1><a href="/" onClick={function(e){
            console.log(e);
            e.preventDefault();
            alert('hi');						// 여기 아래
            // this.state.mode = 'welcome'  
            //오류 2개. 현재 this는 undefined 이니 함수 끝날때 bind 에 선언 + setState 함수 사용해서 해결
            this.setState({
              mode:'welcome'
            });
          }.bind(this)}>{this.state.subject.title}</a></h1>
          {this.state.subject.sub}
        </header>

```



오류 이유

- bind 이해하기

  - 함수에 bind 하면, this를 바꿀 수 있음

  - 

    ```js
    func(){}.bind(aaa)			// func.this === aaa 가 됨
    ```

- 함수 형태로 바꿔야하는 이유
  - App 컴포넌트가 생성되기 전에는 함수를 안써도 되지만, 생성된 뒤에는 `setState` 함수를 써야한다.
  - react 입장에선 함수를 쓰지 않을 경우, 값이 바뀐지를 알 수 없다 => 랜더링할 수 없다.



### 컴포넌트 이벤트 만들기

상속받은 컴포넌트에서 이벤트 넣으려면, `onClick`이 아니라 `onChangePage`를 사용 (이전까진 App.js 컴포넌트에서 직접 이벤트 넣었음)

이후 하위 컴포넌트에서 `onClick` 사용



App.js

```js
        <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub}
          onChangePage={function() {			// 여기부터
            alert('hihi');
            this.setState({mode:'welcome'})
          }.bind(this)}
        >
        </Subject>
```



subject.js

```js
class Subject extends Component {
  render() {

    return (
      <header>
        <h1><a href="/" onClick={function(e){		// 이렇게
          e.preventDefault();
          this.props.onChangePage();    			// 상속받은 이벤트
        }.bind(this)}>{this.props.title}</a></h1>
        {this.props.sub}
      </header>
    )
  }
}
```



원하는 컴포넌트 하위에 표시하기

App.js

```js
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      mode:'read',
      selected_content_id:1,
      subject:{title:"WEB", sub:"world wide web"},
      welcome:{title:'Welcome', desc:'Heelo, React!'},
      contents:[
        {id:1, title:'HTML', desc:'HTML is for information'},
        {id:2, title:'CSS', desc:'CSS is for design'},
        {id:3, title:'JS', desc:'JS is for interactive'},
      ]
    }
  }

  render() {
    var _title, _desc = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if(this.state.mode === 'read') {
      var i = 0;
      while(i < this.state.contents.length) {
        var data = this.state.contents[i];
        if(data.id === this.state.selected_content_id) {
          _title = data.title;
          _desc = data.desc;
          break;
        }
        i = i + 1;
      }
      
      
    }
    return (
      <div className="App">
        <Subject 
          title={this.state.subject.title} 
          sub={this.state.subject.sub}
          onChangePage={function() {
            alert('hihi');
            this.setState({mode:'welcome'})
          }.bind(this)}
        >
        </Subject>
        {/* <header>
          <h1><a href="/" onClick={function(e){
            console.log(e);
            e.preventDefault();
            alert('hi');
            // this.state.mode = 'welcome'  오류 2개. 현재 this는 undefined 이니 함수 끝날때 bind 에 선언 + setState 함수 사용해서 해결
            this.setState({
              mode:'welcome'
            });
          }.bind(this)}>{this.state.subject.title}</a></h1>
          {this.state.subject.sub}
        </header> */}

        <TOC 
          onChangePage={function(id){
            
            this.setState({
              mode:'read',
              selected_content_id:Number(id)
            })
          }.bind(this)} 
          data={this.state.contents}></TOC>
        <Content title={_title} sub={_desc}></Content>
      </div>
    )
  }
}
```



TOC.js

```js
class TOC extends Component{
  render() {

    var lists =  [];
    var data = this.props.data;
    var i = 0;
    while(i < data.length) {
      lists.push(
        <li key={data[i].id}>
          <a 
            href={"/content/"+data[i].id}  
            data-id={data[i].id}    // 'data-' 로 시작하는 변수는 특별히, e 안의 dataset 안에 저장
            onClick={function(e){
              
              e.preventDefault();
              this.props.onChangePage(e.target.dataset.id);    // e.target 은 a 태그를 의미
              this.setState({mode:'read'})
            }.bind(this)}
          >{data[i].title}
          </a>
        </li>)
      i = i + 1;
    
    }
```







## Create 기능



CreateContent.js

```js
      <article>
        <h2>Create</h2>
        <form actios="/create_process" method="post"
          onSubmit={function(e) {				// 여기서 추가
            e.preventDefault();
            this.props.onSubmit(
              e.target.title.value,
              e.target.desc.value
            );

            alert('Submit!')
          }.bind(this)}
        >
          <p><input type="text" name="title" placeholder="title"></input></p>
          <p>
            <textarea name="desc" placeholder='description'></textarea>
          </p>
          <p>
            <input type='submit'></input>
          </p>
        </form>
        
      </article>
```

App.js

```js
  render() {
    var _title, _desc, _article = null;
    if (this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
    } else if(this.state.mode === 'read') {
      var i = 0;
      while(i < this.state.contents.length) {
        var data = this.state.contents[i];
        if(data.id === this.state.selected_content_id) {
          _title = data.title;
          _desc = data.desc;
          break;
        }
        i = i + 1;
      }
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){	// 여기서 추가
        // add content to this.state.contents
        this.max_content_id = this.max_content_id + 1;
        this.state.contents.push(
          {id:this.max_content_id, title:_title, desc:_desc}
        )
        this.setState({
          contents:this.state.contents
      })

        console.log(_title, _desc)
      }.bind(this)}></CreateContent>
    }
```

그런데 push를 쓰면 리소스 관리에 적합하지 않다.

- push는 원본을 바꾸지만, concat은 원본을 바꾸지 않는다. 



shouldComponentUpdate

- `return false` 하면 `render()` 실행 x, `true` 하면 실행함



immutable

- 불변량
- 성능 문제 생기면 찾아보기



## Update, Delete



form 태그 사용