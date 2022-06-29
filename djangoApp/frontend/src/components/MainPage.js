import "./MainPage.css";
import React from "react";
import FAQ from "./FAQ";

class MainPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      question: "",
      asked: false,
      FAQQuestions:[1,1]
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state);
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        "question": event.target.value
      })
    };
    fetch('variants/', requestOptions)
      .then(response => response.json())
      .then(data =>this.setState({FAQQuestions:data.questions,asked:true}));
  }

  render() {
    return (
      <div className="main-page">
        <main>
            <div className="header-panel"></div>
            <div>
              <form className="question-form" onSubmit={this.handleSubmit}>
                <label className="lable">Ask Your Question</label>
                <input
                  className="question-box"
                  placeholder="Enter your question"
                  value={this.state.question}
                  onChange={(e) => { this.setState({ question: e.target.value }) }}
                ></input>
              </form>
            </div>
          </div>
         {this.state.asked && <FAQ questions={this.state.FAQQuestions}/>} 
         </main>
      </div>
    );
  }
}

export default MainPage;
