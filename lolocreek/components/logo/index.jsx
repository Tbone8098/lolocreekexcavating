import cx from 'classnames'
import Image from 'next/image';

// styles
import StyleCSS from './style.module.css'

// images
import Logo from 'images/lolocreeklogo.png';

export default function Index(props) {
    const {width, height} = props


    return (
        <div className={cx(StyleCSS.logo, 'text-center text-2xl')}>
            <Image
            src={Logo}
            width={width}
            height={height}
            />
        </div>
    )
}
