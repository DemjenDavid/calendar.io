import './navbar.css'

export function Navbar() {
    return (
        <nav >
            <a href="/" className="nav_brand">
                Calendar.io
            </a>
            <ul className="nav_menu">
                <li className="nav_item">
                    <a href="/home" className="nav_link">
                        Home
                    </a>
                </li>
                <li className="nav_item">
                    <a href="/home" className="nav_link">
                        Login
                    </a>
                </li>     
            </ul>

        </nav>
    ) 
}
