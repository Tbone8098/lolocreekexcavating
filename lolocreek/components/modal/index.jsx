import cx from 'classnames';
import { useState } from 'react';
import Image from 'next/image';

// styles
import StyleCSS from './style.module.css';

// image
import Close from 'icons/close.png';

const Index = (props) => {
    const {btnText, modal} = props
    const [show, setShow] = useState(false)

    const style = () => {
        if (show) {
            return 'grid grid-col-1 grid-row-1 place-items-center'
        } else {
            return 'hidden'
        }
    }

    const toggleHandler = () => {
        let showCopy = show
        setShow(!showCopy)
    }

    return (
        <div>
            <div className={cx(StyleCSS.wrapper, style())} onClick={toggleHandler}>
                <div className={cx(StyleCSS.modal, 'text-black')} onClick={(e) => e.stopPropagation()}>
                    <div className='justify-end flex m-3' onClick={toggleHandler}>
                        <Image
                        src={Close}
                        alt='close icon'
                        width={50}
                        height={50}
                        />
                    </div>
                    {modal}
                </div>
            </div>
            <p onClick={toggleHandler}>{btnText}</p>
        </div>
    );
}

export default Index;