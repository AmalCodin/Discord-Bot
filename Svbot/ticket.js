module.exports = {
    commands: ['helpticket', 'infoticket'],
    minArgs: 0,
    maxArgs: 0,
    callback: (message, arguments, text) => {
        message.channel.send('Use **!ticket** to open up a __personal__ support channel. The support channel can be used to, ask general questions, report bugs or problems with the server, report a user that is not behaving or that is being innapropriate to you or a fellow user on the server or in a PM. **Please also use the !ticket support channels to report when you are stuck in the Focus Lock.** It is the easiest way for a mod to recognize and help you out!');
    }
}
