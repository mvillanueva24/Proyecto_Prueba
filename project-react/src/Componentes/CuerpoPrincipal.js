import React, { Component, Fragment } from 'react'
import axios from 'axios';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

export class CuerpoPrincipal extends Component {

    state = {
        hoteles: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/hoteles/')
        .then(res => {
            this.setState({ hoteles: res.data });
        })
    }

    render() {
        return (
            <div>
                { this.state.hoteles
                .map(hotel => 
                    <Fragment>
                        <Card style={{ width: '18rem' }}>
                            <Card.Img variant="top" src={"http://127.0.0.1:8000" + hotel.Imagen}/>
                            <Card.Body>
                                <Card.Title>{hotel.Nombre_hotel}</Card.Title>
                                <Card.Text>
                                <b>Ubicacion:</b> {hotel.Ubicacion}
                                </Card.Text>
                                <Card.Text>
                                Calificacion: {hotel.Calificacion}
                                </Card.Text>
                                <Button variant="primary">Go somewhere</Button>
                            </Card.Body>
                        </Card>
                    </Fragment>
                    )
                
                }
            </div>
        )
    }
}

export default CuerpoPrincipal;



