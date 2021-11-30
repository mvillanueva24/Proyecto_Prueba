import React, { Component, Fragment } from 'react'
import CuerpoPrincipal from '../Componentes/CuerpoPrincipal';
import Navbar from '../Componentes/nabvar';
import Habitaciones from '../Componentes/Habitaciones';

class MenuPrincipal extends Component {
    render() {
        return (
            <Fragment>
                <Navbar />
                <CuerpoPrincipal/>
                <Habitaciones />
            </Fragment>
        )
    }
}

export default MenuPrincipal
