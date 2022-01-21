import Header from 'components/header';
import Image from 'next/image';
import { useState, useEffect } from 'react';

// data
import { data } from './data';


export default function Index() {
    const [serviceInfo, setserviceInfo] = useState('')
    const [serviceInfoTitle, setServiceInfoTitle] = useState('')

    useEffect(() => {
        setserviceInfo(data[0].content)
        setServiceInfoTitle(data[0].title)
    }, [])
    
    const actionServiceHandler = (service) => {
        setServiceInfoTitle(service.title)
        setserviceInfo(service.content)
    }

    const style = (service) => {
        if (service.title === serviceInfoTitle){
            return "border-b-4 border-black mb-3"
        } else {
            return "mb-3"
        }
    }

    return (
        <div className='grid grid-cols-12'>
            <div className='col-span-12'>
                <Header />
            </div>
            <div className="col-span-10 col-start-2">
                <div>
                    <ul className='flex justify-evenly'>
                        {
                            data.map((item, key) => {
                                return (
                                    <li key={key}>
                                        <div className={style(item)}>
                                            <Image
                                                src={item.src}
                                                width={item.width}
                                                height={item.height}
                                                onClick={() => actionServiceHandler(item)}
                                            />
                                        </div>
                                    </li>
                                )
                            })
                        }
                    </ul>
                </div>
                <div>
                    <h3 className='text-3xl text-center underline mb-3'>{serviceInfoTitle}</h3>
                    <p>{serviceInfo}</p>
                </div>
            </div>
        </div>
    )
}
