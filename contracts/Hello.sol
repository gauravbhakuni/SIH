// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentDataset {
    struct StudentRecord {
        string courseName;
        string date;
        string certificateUrl;
        string instructorName;
        string studentName;
        string courseLength;
    }

    StudentRecord[] public studentRecords;

    constructor(
        string[] memory _courseNames,
        string[] memory _dates,
        string[] memory _certificateUrls,
        string[] memory _instructorNames,
        string[] memory _studentNames,
        string[] memory _courseLengths
    ) {
        require(
            _courseNames.length == _dates.length &&
            _dates.length == _certificateUrls.length &&
            _certificateUrls.length == _instructorNames.length &&
            _instructorNames.length == _studentNames.length &&
            _studentNames.length == _courseLengths.length,
            "Array lengths must match"
        );

        for (uint256 i = 0; i < _courseNames.length; i++) {
            studentRecords.push(StudentRecord({
                courseName: _courseNames[i],
                date: _dates[i],
                certificateUrl: _certificateUrls[i],
                instructorName: _instructorNames[i],
                studentName: _studentNames[i],
                courseLength: _courseLengths[i]
            }));
        }
    }

    // Function to add a new student record
    function addStudentRecord(
        string memory _courseName,
        string memory _date,
        string memory _certificateUrl,
        string memory _instructorName,
        string memory _studentName,
        string memory _courseLength
    ) public {
        studentRecords.push(StudentRecord({
            courseName: _courseName,
            date: _date,
            certificateUrl: _certificateUrl,
            instructorName: _instructorName,
            studentName: _studentName,
            courseLength: _courseLength
        }));
    }

    // Function to get the number of records
    function getRecordCount() public view returns (uint256) {
        return studentRecords.length;
    }

    // Function to get the details of a student record by index
    function getStudentRecord(uint256 index) public view returns (
        string memory courseName,
        string memory date,
        string memory certificateUrl,
        string memory instructorName,
        string memory studentName,
        string memory courseLength
    ) {
        require(index < studentRecords.length, "Invalid index");
        StudentRecord storage record = studentRecords[index];
        return (
            record.courseName,
            record.date,
            record.certificateUrl,
            record.instructorName,
            record.studentName,
            record.courseLength
        );
    }
}
