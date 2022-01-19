import Image from 'next/image';
import cx from "classnames";

import StyleCSS from './style.module.css';

const Index = (props) => {
    const { img, alt, width, height } = props
    return (
        <div className={cx(StyleCSS.wrapper)}>
            <Image
                src={img}
                alt={alt}
                width={width}
                height={height}
            />
        </div>
    );
}

export default Index;