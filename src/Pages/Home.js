import React, {Component} from 'react';
import Hello from "../Components/Hello";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <Hello msg={this.props.message}/>
      </div>
    );
  }
}

export default Home;