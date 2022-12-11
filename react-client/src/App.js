import React, {UseState, UseEffect}, from 'react'

const App = () => {

    const [data, setData] = useState([{}])

    useEffect(() => {
        fetch("/get_list").then(
            res => res.json()
        ).then{
            data => {
                setData(data)
                console.log(data)
            }
        }
    }, [])

}

export default App;
