import Image from 'next/image';
import { useState, useEffect } from 'react';
import cx from "classnames";

// style
import StyleCSS from './style.module.css';

// data
import { data } from 'datafiles/serviceData';

// components
import { Footer, Header } from 'components';

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
        if (service.title === serviceInfoTitle) {
            return (cx(StyleCSS.active, 'mb-3 bg-lolo-green'))
        } else {
            return "mb-3"
        }
    }

    return (
        <div className='flex flex-col h-screen'>
            <div className='grid grid-cols-12'>
                <div className='col-span-12 md:mt-5 mb-8'>
                    <Header page="services" />
                </div>
                <div className="col-span-10 col-start-2 md:hidden">
                    <div>
                        <ul className='flex justify-evenly'>
                            {
                                data.map((item, key) => {
                                    return (
                                        <li key={key}>
                                            <div className={cx('text-center')} onClick={() => actionServiceHandler(item)}>
                                                <div className={cx(style(item), style, StyleCSS.service__btn, 'flex flex-col w-fit')} >
                                                    <Image
                                                        src={item.src}
                                                        width={item.width}
                                                        height={item.height}
                                                        alt={item.alt}

                                                    />
                                                    <span className='text-xm'>{item.subtitle}</span>
                                                </div>
                                            </div>
                                        </li>
                                    )
                                })
                            }
                        </ul>
                    </div>
                    <div className='md:col-span-2 md:col-start-3 mt-10'>
                        <h3 className='text-3xl text-center underline mb-3'>{serviceInfoTitle}</h3>
                        <span>{serviceInfo}</span>
                    </div>
                </div>
                <div className='hidden md:col-span-8 md:col-start-3 md:flex md:justify-evenly md:flex-wrap'>
                    {
                        data.map((item, key) => {
                            return (
                                <div key={key} className='m-3 p-3 border drop-shadow-lg md:w-full'>
                                    <h3 className='text-3xl font-bold text-center underline mb-3'>{item.title}</h3>
                                    <p>{item.content}</p>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
            <div className='mt-auto'>
                <Footer />
            </div>
        </div>
    )
}
