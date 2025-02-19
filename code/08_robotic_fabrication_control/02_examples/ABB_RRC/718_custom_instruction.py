import compas_rrc as rrc

if __name__ == "__main__":

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, "/rob1")
    print("Connected.")

    # Custom instruction name (RAPID Procedure name), max 80 char
    instruction = "r_RRC_CustomInstruction"

   # string value list of max. 8 strings, max 80 char per string
    string_values = ["Mytext Text"]

   # float value list of max. 36 floats
    float_values = [42]

    # Custom instruction
    done = abb.send_and_wait(rrc.CustomInstruction(instruction, string_values, float_values))

    # Print feedback
    print("Feedback = ", done)

    # End of Code
    print("Finished")

    # Close client
    ros.close()
