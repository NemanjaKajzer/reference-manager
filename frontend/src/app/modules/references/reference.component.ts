
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ReferenceService } from 'src/app/services/reference.service';



@Component({
  selector: 'app-advertisement',
  templateUrl: './reference.component.html',
  styleUrls: ['./reference.component.css']
})
export class ReferenceComponent implements OnInit {

  form: FormGroup;
  filename: String;

  selectedFile: File;

  constructor(private formBuilder: FormBuilder, private referenceService: ReferenceService) {

  }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      document: ['']
    });
  }

  onSubmit() {
    this.referenceService.save(this.selectedFile).subscribe();

    console.log(this.selectedFile);
  }


  onFileSelected(event) {
    console.log(event.target.files);
    this.selectedFile = event.target.files;
  }

}
