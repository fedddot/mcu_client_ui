# Requirements for app McuClientUI
- The application should provide a convenient GUI interface implemented as a python UI application.
- The application receives G-Code commands listing in a multiline text box. The text box should have an arrow pointer pointing to the currently running G-Code command.
- The application has buttons: "play" - run the G-Codes continuosly, "pause" - interrupt the gcodes execution after execution of the running command, "stop" - interrupt the execution and reset the G-Codes execution
- The application should present additionally the following data: UART configuration, current position
# G-Code commands execution
- The application should execute each command by building API requests and receiving API responses to the `McuServer` - a movement server defined with a *.proto filed located at `res/movement_vendor_api.proto`.
- The protocol of communication - request/response over configurable (baud, port name, all the rest are defaults) UART. The application builds the corresponding to a G-Code API Request, serializes it with protobuff library and sends it over the UART. Then it awaits for the response, parses it and takes appropriate actions
# Persistence
- The current application state should be persisted in a *.json file. It should contain:
    - current position (should be updated after each successfull G-Code operation)
    - coordinate mode (absolute/relative)
    - current g-code line
    - an array of all the lines from the text box
- The application should be initialized on the start-up from the persistence data
