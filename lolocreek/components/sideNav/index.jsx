import cx from 'classnames';
import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';

// styles
import StyleCSS from './style.module.css';

// images
import BackwardIcon from 'icons/backward.png';
import ForwardIcon from 'icons/forward.png';

// components
import {data} from './data';

const Index = () => {
    const [isOpen, setIsOpen] = useState(false)

    const toggleOpen = () => {
        let temp = isOpen
        setIsOpen(!temp)
    }
    
    const hamburger = () => {
        return (
            <div className={cx(StyleCSS.wrapper)} onClick={toggleOpen}>
                <div className={cx(StyleCSS.hamburger)}>
                    <span></span>
                </div>
            </div>
        )
    }
    
    const menu = () => {
        return (
            <div className={cx(StyleCSS.menu, 'flex flex-col')}>
                <div className='mt-4'>
                    <Image
                    src={BackwardIcon}
                    width={50}
                    height={50}
                    onClick={toggleOpen}
                    />
                </div>
                <ul className='m-auto'>
                    {
                        data.map((item, key) => {
                            return (
                                <li className='mb-3' key={key}>
                                    <div className='place-items-center flex gap-2'>
                                        <Image 
                                        alt={item.alt}
                                        src={item.src}
                                        width={item.width}
                                        height={item.height}
                                        />
                                        <Link href={item.url}>
                                            {item.title}
                                        </Link>
                                    </div>
                                </li>
                            )
                        })
                    }
                </ul>
            </div>
        )
    }

    return (
        <>
            {
                isOpen && menu()
            }
            {hamburger()}
        </>
    );
}

export default Index;