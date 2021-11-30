import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component, Fragment } from 'react';
import axios from 'axios';
import CardGroup from 'react-bootstrap/CardGroup';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';



export class Habitaciones extends Component {

    state = {
        habitaciones: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/habitaciones/')
        .then(res => {
            this.setState({ habitaciones: res.data });
        })
    }

    render() {
        return (
            <div>
                { this.state.habitaciones.map(habitaciones =>
                        <Fragment>
                            <CardGroup>
                                <Card>
                                    <Card.Img variant="top" src={"http://127.0.0.1:8000" + habitaciones.Imagen} />
                                    <Card.Body>
                                    <Card.Title>Habitacion Familiar</Card.Title>
                                    <Card.Text>
                                    <h3>Numero habitacion:</h3>{habitaciones.Nro_habitacion}
                                    </Card.Text>
                                    <Card.Text>
                                        {habitaciones.Estado_habitacion}
                                        {habitaciones.Cerradura_electronica}
                                    </Card.Text>
                                    </Card.Body>
                                </Card>
                                </CardGroup>
                        </Fragment>
                        )
                    }
            </div>
        )
    }
}

export default Habitaciones;



