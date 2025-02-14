import React, {Component, PropTypes} from "react"
import {connect} from "react-redux"
import {Link} from "react-router"

import {Header} from "../Components/basic_components/header.jsx"
import {Footer} from "../Components/basic_components/footer.jsx"
import {TocHero, TocContent} from "../Components/toc_components/toc.jsx"

const mapStateToProps = (state) => {
    return {authed: state.authed}
}

export class TocContainer extends Component {
    static propTypes = {
        authed: PropTypes.object.isRequired,
        location: PropTypes.object.isRequired,
        onLogoutClick: PropTypes.func.isRequired
    }

    constructor(props) {
        super(props)
    }

    render() {
        const {authed, location, onLogoutClick} = this.props
        return (
            <div className="misc-page">
                <Header
                    authed={authed}
                    location={location.pathname}
                    onLogoutClick={onLogoutClick}
                    >
                        <Link to={"/faq/"}>Aide</Link>
                        <Link to={"/toc/"}>Responsabilités</Link>
                        <Link to={"/about/"}>Nous connaître</Link>
                </Header>
                <TocHero/>
                <TocContent/>
                <Footer/>
            </div>
        )
    }
}

export default connect(mapStateToProps)(TocContainer)
