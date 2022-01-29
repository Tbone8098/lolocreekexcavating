import { Header, Footer } from 'components';
import { useState, useRef } from 'react';
import emailjs from '@emailjs/browser';

export default function Index() {
    const [fullname, setFullname] = useState('')
    const [email, setEmail] = useState('')
    const [message, setMessage] = useState('')

    const [fullnameError, setFullnameError] = useState('')
    const [emailError, setEmailError] = useState('')
    const [messageError, setMessageError] = useState('')

    let EMAILRE = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)

    const typeHandler = (e) => {
        const name = e.target.getAttribute('name')
        let stateName = 'set' + name[0].toUpperCase() + name.slice(1)
        let content = e.target.value 
        eval(stateName)(content)

        if (name === 'fullname'){
            fullnameHandler(e)
        } else if (name === 'email') {
            emailHandler(e)
        } else {
            messageHandler(e)
        }
    }

    const fullnameHandler = (e) => {
        let content = e.target.value
        let lengthRequirement = 5
        if (content === ''){
            setFullnameError('')
        }
        else if (content.length <= lengthRequirement){
            setFullnameError(`You need ${lengthRequirement - content.length } more characters`)
        } else {
            setFullnameError('')
        }
    }

    const emailHandler = (e) => {
        if (e.target.value === ''){
            setEmailError('')
        }else if (!EMAILRE.test(e.target.value)){
            setEmailError('Invalid Email')
        } else {
            setEmailError('')
        }
    }

    const messageHandler = (e) => {
        let content = e.target.value
        let lengthRequirement = 15
        if (content === ''){
            setMessageError('')
        } else if (content.length <= lengthRequirement){
            setMessageError(`You need ${lengthRequirement - content.length} more characters`)
        } else {
            setMessageError('')
        }
    }


    const form = useRef();

    const sendEmail = (e) => {
      e.preventDefault();
      console.log(form.current);
  
    //   emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', form.current, 'YOUR_USER_ID')
    emailjs.sendForm('service_z7obine', 'template_b7ge82t', form.current, 'user_eOeta8I5Ss7MwEOB81mgt')
        .then((result) => {
            console.log(result.text);
        }, (error) => {
            console.log(error.text);
        });
    };


    return (
        <div className="flex flex-col h-screen">
            <div className='grid grid-col-12'>
                <div className='col-span-12 mt-5'>
                    <Header />
                </div>
                <div className='col-span-10 col-start-2 md:mt-32'>
                    <h2 className="text-2xl text-center md:text-5xl">Send Us a Message</h2>
                    <form className='flex flex-col items-center md:mt-8' method="post" ref={form} onSubmit={sendEmail}>
                        <div className='w-full grid md:grid-cols-2 gap-3 items-center md:flex-row md:justify-between'>

                            <div className='flex flex-col mb-3'>
                                <input className='border w-full text-center md:w-full p-5 md:mr-3' type="text" name="fullname" id="fullname" placeholder='Fullname' value={fullname} onChange={(e) => typeHandler(e)} />
                                <span className='text-center'>{fullnameError}</span>
                                
                            </div>
                            <div className='flex flex-col mb-3'>
                                <input className='border w-full text-center md:w-full p-5 ' type="text" name="email" id="email" placeholder='Email' value={email} onChange={(e) => typeHandler(e)} />
                                <span className='text-center'>{emailError}</span>
                            </div>

                        </div>
                        <div className='w-100 mb-3 w-full md:flex md:flex-col'>

                            <textarea name="message" id="message" cols="30" rows="10" className='border w-full' onChange={(e) => typeHandler(e)} value={message} placeholder='Message'></textarea>
                            <span className='text-center'>{messageError}</span>
                        </div>
                        <input type='submit' value='Submit' className='border bg-orange-500 p-3 w-full lg:w-1/2'/>
                    </form>
                </div>
            </div>
            <div className='mt-auto'>
                <Footer />
            </div>
        </div>
    )
}
