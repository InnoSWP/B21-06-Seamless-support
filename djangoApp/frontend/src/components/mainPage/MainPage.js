// import React, {useState} from "@types/react";
//
// const MainPage = (props) =>{
//
//     constructor(props) {
//         super(props);
//         this.state = {
//             question: ""
//         };
//         this.handleSubmit = this.handleSubmit.bind(this);
//     }
//     [question, setQuestion] = useState('ik')
//     handleSubmit(event){
//         event.preventDefault();
//         console.log(this.state);
//         const requestOptions = {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({
//                 "question": event.target.value
//             })
//         };
//         fetch('', requestOptions)
//             .then(response => response.json())
//             .then(data => console.log(data));
//     }
//
//         return (
//             <div className="App">
//                 <main>
//                     <div>
//                         <div className="header-panel">Header Panel</div>
//                         <div>
//                             <form className="question-form" onSubmit={this.handleSubmit}>
//                                 <label className="lable">Ask Your Question</label>
//                                 <input
//                                     className="question-box"
//                                     placeholder="Enter your question"
//                                     value={this.state.question}
//                                     onChange={(e) => { this.setState({ question: e.target.value }) }}
//                                 ></input>
//                             </form>
//                         </div>
//                     </div>
//                 </main>
//             </div>
//         );
// }
//
// export default MainPage