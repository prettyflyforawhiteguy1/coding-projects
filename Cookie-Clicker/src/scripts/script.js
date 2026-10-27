 let cookies = 0
 let clicks = 0
 let multiplier = 1
 let m_upgradecost = 10
 const cookietext = document.getElementById("cookiesmade")
 const multipliertext = document.getElementById("multiplier")
 const m_ucosttext = document.getElementById("nextupg")
function makecookie() {
    clicks++
    console.log("Clicks:", clicks)
    cookies += multiplier
    cookietext.textContent = cookies
    if (cookies < 0){
        cookies = 0
    }
    if (cookies >= m_upgradecost) {
        upgradebuttontoggle(false)
    } else{
        upgradebuttontoggle(true)
    }
    return multiplier, cookies
}

function upgradebuttontoggle(a) {
    const upgbtn = document.getElementById("upbtn")
    if (!upgbtn) {
        console.error('No element found with id="upbtn"')
        return;
    }
    upgbtn.disabled = a
}
function m_upgrade(){
    cookies = cookies - m_upgradecost
    cookietext.textContent = cookies
    multiplier *= 2
    multipliertext.textContent = multiplier
    m_upgradecost *= 4
    m_ucosttext.textContent = m_upgradecost
}
