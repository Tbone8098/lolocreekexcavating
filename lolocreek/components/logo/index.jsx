import cx from 'classnames'
import Image from 'next/image';

// styles
import StyleCSS from './style.module.css'

export default function Index(props) {
    const {img, width, height} = props
    
    return (
        <div className={cx(StyleCSS.logo, 'text-center text-2xl')}>
            <Image 
            src={img}
            width={width}
            height={height}
            />
        </div>
    )
}
