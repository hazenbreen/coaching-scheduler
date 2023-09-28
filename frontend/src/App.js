import 'devextreme/dist/css/dx.light.css';
import './App.css';
import React from 'react';
import Scheduler from 'devextreme-react/scheduler';
import List from 'devextreme-react/list';
import axios from 'axios';



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state={
      coaches:['No coaches available'],
      students:['No students available'],
      selectedCoach:'',
      timeSlots:[],
      selectedTimeSlot: {},
    }
    this.setSelectedCoach = this.setSelectedCoach.bind(this);
    this.setSelectedTimeSlot = this.setSelectedTimeSlot.bind(this);
    this.onAppointmentFormOpening = this.onAppointmentFormOpening.bind(this);
    // this.onAppointmentUpdated = this.onAppointmentUpdated.bind(this);
  }

  componentDidMount() {
    this.refreshCoaches();
    this.refreshStudents();
  }

  refreshCoaches = () => {
    axios
      .get("/api/coaches/")
      .then((res) => this.setState({ coaches: res.data }))
      .catch((err) => console.log(err));
  };

  refreshStudents = () => {
    axios
      .get("/api/students/")
      .then((res) => this.setState({ students: res.data }))
      .catch((err) => console.log(err));
  };

  refreshCoachTimeSlots = (coachName) => {
    let coach = this.state.coaches.find((coach => coach.name === coachName))
    axios
      .get("/api/timeslots", {headers:{coach: coach.id}})
      .then((res) => this.setState({ timeSlots: res.data }))
      .catch((err) => console.log(err));
  }  

  render() {
    return (
      <React.Fragment>
        <div className="widget-container">
          <List
            dataSource={this.state.coaches.map(coach => coach.name)}
            selectionMode="single"
            onItemClick={this.setSelectedCoach}
          />
        </div>
        <div className='widget-container'>
          <Scheduler
            cellDuration={120}
            allDayPanelMode={'hidden'}
            textExpr="student"
            onAppointmentFormOpening={this.onAppointmentFormOpening}
            onAppointmentUpdated={this.onAppointmentUpdated}
            dataSource={this.state.timeSlots}
          />
        </div>
      </React.Fragment>
    );
  }

  onAppointmentFormOpening(e) {
    const { form } = e;
    let studentNames = this.state.students.map(student => student.name)

    form.option('items', [{
      label: {
        text: 'Student',
      },
      editorType: 'dxSelectBox',
      dataField: 'student',
      editorOptions: {
        width: '100%',
        items: studentNames,
      },
    },
    {
      label: {
        text: 'Coach',
      },
      editorType: 'dxTextBox',
      editorOptions: {
        width: '100%',
        value: this.state.selectedCoach,
        readOnly: true,
      },
    },  
    {
      dataField: 'startDate',
      editorType: 'dxDateBox',
      editorOptions: {
        type: 'datetime',
        readOnly: true,
      },
    }, {
      name: 'endDate',
      dataField: 'endDate',
      editorType: 'dxDateBox',
      editorOptions: {
        type: 'datetime',
        readOnly: true,
      },
    },
    ]);
  }

  setSelectedCoach(e) {
    this.setState({ selectedCoach: e.itemData })
    this.refreshCoachTimeSlots(e.itemData)
  }

  setSelectedTimeSlot(e) {
    this.setState({ selectedTimeSlot: e.itemData })
  }

  // TODO: add PUT to update appointment with student
  // onAppointmentUpdated(e) {
  //   axios
  //     .put("/api/timeslots/")
  //     .catch((err) => console.log(err));
  // }
}

export default App;
