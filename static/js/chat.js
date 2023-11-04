
const o = document.querySelector(".app-chat-contacts .sidebar-body");
const i = document.querySelector(".chat-history-body");
const u = document.querySelector(".app-chat-sidebar-left .sidebar-body");
const d = document.querySelector(".app-chat-sidebar-right .sidebar-body");

if (o) {
  new PerfectScrollbar(o, { wheelPropagation: !1, suppressScrollX: !0 });
}

if (i) {
  new PerfectScrollbar(i, { wheelPropagation: !1, suppressScrollX: !0 });
}

if (u) {
  new PerfectScrollbar(u, { wheelPropagation: !1, suppressScrollX: !0 });
}

if (d) {
  new PerfectScrollbar(d, { wheelPropagation: !1, suppressScrollX: !0 });
}
function a() {
    i.scrollTo(0, i.scrollHeight);
  }

a(); // Llama a la función para desplazarse al final del chat


const dashboarsSlug = document.getElementById('dashboard-slug').textContent.trim();
const userDom = document.getElementById('user').textContent.trim();
const submitBtn = document.getElementById('submit-btn');
const dataInput = document.getElementById('data-input');
const chatMenssage = document.getElementById('chatmenssage');
const chatListUser = document.getElementById('chat-list');


function connectToWebSocket() {
    const socket = new WebSocket(`ws://${window.location.host}/ws/view/${dashboarsSlug}/`);
    console.log(socket);
    // Manejar el evento onopen
    socket.onopen = function (e) {
        console.log("Successfully connected to the WebSocket.");
    };

    // socket.onclose = function (e) {
    //     console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
    //     setTimeout(function () {
    //         console.log("Reconnecting...");
    //         // Vuelve a conectar aquí llamando a la función que establece la conexión.
    //         connectToWebSocket();
    //     }, 2000);
    // };
    
    socket.onmessage = function(e){
        const data = JSON.parse(e.data)
        switch (data.type) {
            case "chat_message":
                chatMenssage.innerHTML += `<li class="chat-message ${data.user === userDom ? 'chat-message-right' : ''}">
                                                <div class="d-flex ove  rflow-hidden">  
                                                    ${data.user !== userDom ? '<div class="user-avatar flex-shrink-0 ms-3"><div class="avatar avatar-sm"><span class="avatar-initial rounded-circle bg-label-success">'+data.user+'</span></div></div>' : ''}
                                                    <div class="chat-message-wrapper flex-grow-1">
                                                        <div class="chat-message-text">
                                                            <p class="mb-0">
                                                                ${data.message}
                                                            </p>
                                                        </div>
                                                        <div class="text-end text-muted mt-1">
                                                            <i class="bx bx-check-double text-success"></i>
                                                            <span class="time">Ahora</span>
                                                        </div>
                                                    </div>
                                                    ${data.user === userDom ? '<div class="user-avatar flex-shrink-0 ms-3"><div class="avatar avatar-sm"><span class="avatar-initial rounded-circle bg-label-success">'+data.user+'</span></div></div>' : ''}
                                                </div>
                                            </li>`
                break;
                
            case "user_join":
                chatListUser.innerHTML = "";
                for (var i = 0; i < data.user.length; i++) {
                    
                    chatListUser.innerHTML += `<li class="chat-contact-list-item" id="${data.user[i]}">
                                                    <a class="d-flex align-items-center">
                                                        <div class="flex-shrink-0 avatar avatar-online">
                                                            <span class="avatar-initial rounded-circle bg-label-success">CM</span>
                                                        </div>
                                                        <div class="chat-contact-info flex-grow-1 ms-3">
                                                            <h6 class="chat-contact-name text-truncate m-0">
                                                                ${data.user[i]}
                                                            </h6>
                                                        </div>
                                                    </a>
                                                </li>`
                }
                break;

            case "user_leave":
                var elemento = document.getElementById(data.user);
                elemento.parentNode.removeChild(elemento);
                break;
                            
            default:
                console.error("Unknown message type!");
                break;
        
        }

    }

    submitBtn.addEventListener('click', () => {
        sendMessage();
    });

    dataInput.addEventListener('keydown', (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const dataValue = dataInput.value;

        // Verificar si el campo de entrada está vacío
        if (dataValue.trim() !== "") {
            socket.send(JSON.stringify({
                'message': dataValue,
            }));
            dataInput.value = "";
            dataInput.focus();
            a();
        }
    }
}

connectToWebSocket();
