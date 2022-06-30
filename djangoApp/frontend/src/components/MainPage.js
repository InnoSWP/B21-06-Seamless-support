import "./MainPage.css";
import React from "react";
import FAQ from "./FAQ";
import axios from "axios";

class MainPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currQuestion: "",
            asked: false,
            FAQQuestions: [

            ]
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.state);
        axios(
            {
                method: "POST",
                url: "variants/",
            }
        ).then((response) => {
            const data = response.data
            console.log(data)
            this.setState({FAQQuestions: data, asked: true}, )
        }
        )
        console.log(this.state.FAQQuestions);
    }

    changeHandling = (index, params) => {
        this.props.onPage(index, params);
    }
    render() {
        return (
            <div className="main-page">
                <main>
                    <div className="header-panel"/>
                    <div>
                        <form className="question-form" onSubmit={this.handleSubmit}>
                            <label className="lable">Ask Your Question</label>
                            <input
                                className="question-box"
                                placeholder="Enter your question"
                                value={this.state.question}
                                onChange={(e) => {
                                    this.setState({currQuestion: e.target.value})
                                }}
                            />
                        </form>
                    </div>
                    <FAQ questions={this.state.FAQQuestions} question={this.state.currQuestion} onChoose={this.changeHandling}/>
                </main>
            </div>
        );
    }
}

export default MainPage;
