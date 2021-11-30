import React, {Component} from 'react';

import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'

class navbar extends Component {
    state = {
        categorias: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/categorias/')
        .then(res => {
            this.setState({ categorias: res.data });
        })
    }

    render() {
        return (
            <div>
                <Navbar bg="dark" variant="dark">
                    <Container>
                    <Nav className="me-auto">
                        { 
                        this.state.categorias
                        .map(categoria => 
                            <Nav.Link key={categoria} href="#pricing">{categoria.Nombre_categoria}</Nav.Link>
                        )
                        }
                        
                    </Nav>
                    </Container>
                </Navbar>
            </div>
        )
    }
}

export default navbar;