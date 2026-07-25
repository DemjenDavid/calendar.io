import './App.css'
import { Navbar } from './navbar';
import { Calendar } from 'rsuite';
import 'rsuite/Calendar/styles/index.css'

function App() {
  return ( 
    <div>
      <Navbar />
      <Calendar />
    </div>
  )
}

export default App
