// const electron = require('electron')

// 애플리케이션 생명 주기는 electron.app을 통해 관리되며, 
// electron.BrowserWindow 클래스를 사용하여 창을 생성할 수 있다.
const { app, BrowserWindow } = require('electron')

// window 객체는 전역 변수로 유지한다, 객체가 가비지 콜렉트될 때 창이 닫히지 않도록.

let win
function createWindow () {
    // 브라우저 창을 생성
    win = new BrowserWindow({ width: 800, height: 600 })

    // 앱의 index.html 파일을 로드
    win.loadFile('index.html')

    // 개발자 도구 열기
    win.webContents.openDevTools()

    // 창이 닫힐 때 발생
    win.on('closed', () => {
        // window 객체에 대한 참조해제
        // 창을 배열에 저장할 수 있다.
        win = null
    })
}

// Electron이 초기화를 마치고 브라우저 창을 생성할 준비가 되었을 때 호출
app.on('ready', createWindow)

// 모든 창이 닫혔을 때 종료
app.on('window-all-closed', () => {
    // 일반적으로 macOS에서는 사용자가 cmd + Q 누르기 전까지 애플리케이션이 활성화되어 있다.
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    // macOS에서 dock 아이콘이 클릭될 때(activate) 다른 윈도우가 열려있지 않는다면
    // 앱에서 새 창을 여는 것이 일반적이다.
    if (win == null) {
        createWindow()
    }
})